import os
import olympe
from olympe.messages.camera2.Command import Configure, StartPhoto
from olympe.messages.camera2.Event import Photo

DRONE_IP = os.environ.get('DRONE_IP', '10.202.0.1')


def test_photo():
    with olympe.Drone(DRONE_IP) as drone:
        drone.connect()
        drone(
            Configure(camera_id=0,
                      config=dict(
                          camera_mode='photo',
                          photo_mode='single',
                          photo_format='full_frame',
                          photo_file_format='jpeg',
                          photo_dynamic_range='standard',
                          exposure_mode='automatic',
                          white_balance_mode='automatic',
                          ev_compensation='0_00',
                      )) >> StartPhoto(camera_id=0) >> Photo(
                          camera_id=0,
                          type='taking_photo',
                      ) >> Photo(
                          camera_id=0,
                          type='stop',
                          stop_reason='capture_done',
                      )).wait()
        drone.disconnect()


if __name__ == '__main__':
    test_photo()