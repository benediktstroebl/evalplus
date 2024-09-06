def file_name_check(file_name):
    lilies, ext = 0, 0
    dot_index = file_name.find(".")
    if dot_index==-1 or len(file_name)<=dot_index+1 or not file_name[0].isalpha():
        return "No"
    lilies = file_name[:dot_index]
    ext = file_name[dot_index+1:]
    if lilies[:-1].count("0123456789")>3 or ext not in ["txt", "exe", "dll"] or lilies[-1]==".":
        return "No"
    return "Yes"