def unique_digits(x):
    """Given a list of positive integers x.
    
    - returns a unique sorted elements without any even digit
    """
    y = []
    for num in x:
        # remove all even digits
        num_str = str(num)
        even_pos = num_str.find('0')
       
        num_str = num_str[:even_pos] + num_str[even_pos+1:]
        y.append(int(num_str))
    
    return sorted(y)