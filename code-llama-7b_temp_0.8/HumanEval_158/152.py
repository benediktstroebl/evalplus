
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here
    #Set() is a predefined python method to create a set
    # The set method creates a set of unique elements
    #set method returns a set of unique elements
    #return max(set(words), key=words.count)
    #using the set method to find the unique elements
    max=0
    ans=""
    for i in words:
        u=len(set(i))
        if u>max:
            max=u
            ans=i
    return ans
    
