def fruit_distribution(s, n):
    """
    Distributes fruits from a basket described in a string into apples, oranges, and mangoes.

    Parameters:
    s (str): Description of the number of apples and oranges in the format "X apples and Y oranges".
    n: Total number of fruits in the basket.

    Returns:
    int: Number of mangoes in the basket.
    """
    # Split the sentence to extract numbers.
    words = s.split() 
    apples = int(words[0].replace("apples", ""))
    oranges = int(words[3].replace("oranges", ""))

    # Calculate the number of mangoes.
    return n - apples - oranges