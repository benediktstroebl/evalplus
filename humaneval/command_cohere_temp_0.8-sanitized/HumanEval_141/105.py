def file_name_check(file_name):
    checker = []
    
    # There should not be more than three digits ('0'-'9') in the file's name
    num_digits = sum(1 for c in file_name if c.isdigit())
    checker.append(num_digits <= 3)
    
    # The file's name contains exactly one dot '.'
    checker.append('.' not in file_name or file_name.count('.') == 1)
    
    # The substring before the dot should not be empty, and it starts with a letter from 
    # the latin alphapet ('a'-'z' and 'A'-'Z').
    prev_dot = file_name.rindex('.')
    checker.append(prev_dot != -1 and file_name[:prev_dot] and 
                   file_name[:prev_dot][0].isalpha())
    
    # The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    checker.append(set(['.txt', '.exe', '.dll']) >= set(file_name[prev_dot+1:]))
    
    if all(checker):
        return 'Yes'
    else:
        return 'No'