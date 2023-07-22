from pathlib import Path

group_temp_path = Path(r"D:\xx\Documents\Tencent Files\xxxxx\Image_Group_Temp")

# everything x64 1.5 alpha 支持efu列表缩略图
# everything ini 文件设置 filelist_thumbnails=1

def generate_efu_data(data):
    header = ["Filename","Size"]
    _file_list = []
    _file_list.append(','.join(header))

    for line in data:
        dst_path = line.split(",")[3]
        _path = Path(dst_path)
        try:
            filesize = _path.stat().st_size
            _last_line = [str(_path), str(filesize)]
            _file_list.append(','.join(_last_line))
        except FileNotFoundError:
            continue
    
    return _file_list

csv_file_list = [csv_file for csv_file in group_temp_path.iterdir() if csv_file.suffix == '.csv']

for csv_file in csv_file_list:
    with open(csv_file, mode="r", encoding="utf-8-sig") as f:
        _data = f.readlines()
    print(csv_file.name)

    _efu_data = generate_efu_data(_data)
    with open(csv_file.with_suffix(".efu"), mode='w', encoding='utf-8') as f:
        f.write('\n'.join(_efu_data))

input("done")
