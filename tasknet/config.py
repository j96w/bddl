import os 

TASK_CONFIGS_PATH = 'C:\\Users\\igibs\\TaskNet\\tasknet\\task_configs\\'
SCENE_PATH = 'd:\\ig_dataset\\scenes'
OBJECT_MODEL_PATH = 'D:\\gibson2_assets\\processed'


def get_object_filepath(obj_category_instance):
    '''
    Generate object filename
    NOTE check if this needs to change
    '''
    return os.path.join(OBJECT_MODEL_PATH, object_category_instance, 'rigid_body.urdf')




