def file_name_check(file_name):
    lat_let = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    conditions = [
        lambda: len(file_name) > 0,
        lambda: '.' in file_name,
        lambda: file_name.split(".")[0].startswith(lat_let),
        lambda: len(file_name.split(".")[1]) in [1, 2] and file_name.split(".")[1].lower() in ['txt', 'exe', 'dll']
    ]
    
    return "Yes" if all(condition() for condition in conditions) else "No"