def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    # Splitting the string into a list of words
    words = s.split()
    
    # Initializing variables to store the numbers of apples and oranges
    num_apples = 0
    num_oranges = 0
    
    # Looping through the words to determine the number of apples and oranges
    for i in range(len(words)):
        if words[i] == "apples":
            num_apples = int(words[i-1])
        elif words[i] == "oranges":
            num_oranges = int(words[i-1])
    
    # Calculating the number of mango fruits
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes
