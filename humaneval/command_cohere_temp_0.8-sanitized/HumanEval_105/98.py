def by_length(arr):
    # Sort the array arr in ascending order
    sorted_arr = sorted(arr)
    
    # Create a list called filtered_digits that contains only the elements from arr that are between 1 and 9 (inclusive)
    filtered_digits = [ele for ele in sorted_arr if 1 <= ele <= 9]
    
    # Reverse the filtered_digits list (this will also reverse the elements within it)
    reversed_digits = filtered_digits[::-1]
    
    # Create a list called digit_names containing the names of the digits from 'One' to 'Nine'
    digit_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    
    # Use a list comprehension to iterate through digit_names, returning the elements at the indices that correspond to the elements in reversed_digits
    return