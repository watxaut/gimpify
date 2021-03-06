import os
from pathlib import Path
from shutil import copyfile

from .context import gimpify, parent_path


def test_create_face_json():
    folder_path = Path(f"{parent_path}/resources/test/faces").absolute()
    json_path = folder_path / "faces.json"
    gimpify.montage.create_face_json(folder_path, json_path, just_update=False)
    assert os.path.isfile(json_path)  # check it exists


def test_create_backgrounds_json():
    folder_path = Path(f"{parent_path}/resources/test/backgrounds").absolute()
    json_path = folder_path / "backgrounds.json"
    gimpify.montage.create_background_json(folder_path, json_path, just_update=False)
    assert os.path.isfile(json_path)  # check it exists


def test_create_random_montage():
    montage_folder_path = Path(f"{parent_path}/resources/test/tmp").absolute()
    for s_filename in os.listdir(montage_folder_path):  # remove files in tmp
        os.remove(montage_folder_path / s_filename)

    backgrounds_path = Path(f"{parent_path}/resources/test/backgrounds/backgrounds.json").absolute()
    faces_path = Path(f"{parent_path}/resources/test/faces/faces.json").absolute()
    only_face = False
    gimpify.montage.create_random_montage(montage_folder_path, backgrounds_path, faces_path, only_face)
    l_files = [img for img in os.listdir(montage_folder_path) if str(img).endswith(".png")]
    assert len(l_files) == 1


def test_create_montage_with_background():
    montage_folder_path = Path(f"{parent_path}/resources/test/tmp").absolute()
    for s_filename in os.listdir(montage_folder_path):  # remove files in tmp
        os.remove(montage_folder_path / s_filename)

    im_background_path = Path(f"{parent_path}/resources/test/backgrounds/theoffice.png").absolute()
    faces_path = Path(f"{parent_path}/resources/test/faces/faces.json").absolute()
    only_face = False
    gimpify.montage.create_montage_for_background(montage_folder_path, im_background_path, faces_path, only_face)
    l_files = [img for img in os.listdir(montage_folder_path) if str(img).endswith(".png")]
    assert len(l_files) == 1


def test_create_face_json_just_update():
    folder_path = Path(f"{parent_path}/resources/test/faces").absolute()
    json_path = folder_path / "faces.json"
    boy_tmp = folder_path / "boy_tmp.png"
    boy_img = folder_path / "boy.png"
    copyfile(boy_img, boy_tmp)  # creates a new img
    if os.path.isfile(json_path):
        os.remove(json_path)
    gimpify.montage.create_face_json(folder_path, json_path, just_update=True)

    os.remove(boy_tmp)  # removes boy
    assert os.path.isfile(json_path)  # check it exists


def test_create_backgrounds_json_just_update():
    folder_path = Path(f"{parent_path}/resources/test/backgrounds").absolute()
    json_path = folder_path / "backgrounds.json"
    boy_tmp = folder_path / "boy1_tmp.png"
    boy_img = folder_path / "boy1.png"
    copyfile(boy_img, boy_tmp)  # creates a new img
    if os.path.isfile(json_path):
        os.remove(json_path)
    gimpify.montage.create_background_json(folder_path, json_path, just_update=True)

    os.remove(boy_tmp)  # removes boy
    assert os.path.isfile(json_path)  # check it exists
