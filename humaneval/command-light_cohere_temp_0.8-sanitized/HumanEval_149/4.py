def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the list by the length of each word, ascending
    sorted_filtered_lst = sorted(filtered_lst, key=len, reverse=False)
    
    # Concatenate all the sorted words
    return ' '.join(sorted_filtered_lst)