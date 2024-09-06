def file_name_check(file_name):
    loot = []
    dig = ['0','1','2','3','4','5','6','7','8','9']
    lat = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ext = ['txt', 'exe', 'dll']
    if len(file_name) > 0:
        num = file_name.count('.')
        if len(file_name) != 1 or num != 1:
            loot.append(0)
        elif file_name[0] in lat and file_name[-3:] in ext:
            loot.append(1)
        elif file_name[0] in dig or file_name[0] in ['_', '.', '~', '-']:
            loot.append(0)
        elif file_name.split('.')[0].strip() == '':
            loot.append(0)
    else:
        loot.append(0)
    if sum(loot) == 1:
        return 'Yes'
    else:
        return 'No'