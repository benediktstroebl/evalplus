def file_name_check(file_name):
    dot_index = file_name.find(".")
    if dot_index==-1:
        return "No"
    left_part = file_name[:dot_index]
    right_part = file_name[dot_index+1:]
    if len(left_part)==0 or not left_part[0].isalpha():
        return "No"
    if len(right_part)==0 or (right_part!="txt" and right_part!="exe" and right_part!="dll"):
        return "No"
    digit_count = 0
    for char in file_name:
      if char.isdigit():
        digit_count += 1
    if digit_count>3:
        return "No"
    return "Yes"