def file_name_check(file_name):
    checker = [](
        lambda : len(re.findall(r'\d{4,}', file_name)) <= 0,
        lambda : '.' in file_name,
        lambda : file_name.split('.')[0].lower() != '',
        lambda : file_name.split('.')[1] in ['txt', 'exe', 'dll']
    )
    return 'Yes' if all(checker) else 'No'