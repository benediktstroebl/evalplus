def file_name_check(file_name):
    merits = 5
    demerits = 0

    # Checking if the file name contains exactly one dot '.'
    if ('.' in file_name) != 1:
        demerits += 1

    # Counting the number of digits present in the file's name
    digits_count = file_name.replace('.', '').count('0123456789')
    
    # Giving full marks if the count is less than or equal to 2 and deducting 2 points if greater
    merits -= min(2, digits_count)
    demerits += max(0, 2 - digits_count)

    # Checking if the substring before the dot is empty or does not start with a latin letter
    if not file_name.split('.')[0]:
        demerits += 1
    if file_name.split('.')[0][0].isalpha():
        merits += 1

    # Checking if the substring after the dot is one of the expected ['txt', 'exe', 'dll']
    if file_name.split('.')[1] in ['txt', 'exe', 'dll']:
        merits += 1
    else:
        demerits += 1

    # Returning the conclusion based on the total marks
    if merits > demerits:
        return 'Yes'
    else:
        return 'No'