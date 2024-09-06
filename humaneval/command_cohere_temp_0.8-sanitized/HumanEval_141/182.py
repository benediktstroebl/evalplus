def file_name_check(file_name):
    checker = [str(file_name).count('0123456789'), 
              len(file_name.split('.')[0]) == 0 or (file_name.split('.')[0][0].isalpha() and 
                                               file_name.split('.')[0][1:].isalnum()),
              file_name.split('.').count('.') == 1,
              set(file_name.split('.')[1:]) == set(['txt', 'exe', 'dll'])]
    
    if checker.count(True) == len(checker):
        return "Yes"
    else: 
        return "No"