
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    
    def create_dict(test):
        # create a dictionary with the repetitions of each letter
        dict_test = {}
        # check each element from the test
        for el in test.split():
            # check if the element exists in the dict
            if el in dict_test.keys():
                # if so, add one to the counter
                dict_test[el] += 1
            else:
                # if not, create it and set it to 1
                dict_test[el] = 1
        return dict_test
    
    def find_most_repeated(test):
        # create the dictionary with the repetitions
        dict_test = create_dict(test)
        # create a dict with the values of repetitions
        val_dict = {}
        # and fill it with the values of dict_test
        for k, v in dict_test.items():
            val_dict[v] = k
        # create a list with the repetitions
        repetitions = list(dict_test.values())
        # create a list with the keys
        keys = list(dict_test.keys())
        # create a list with the values of dict_test
        values = list(val_dict.keys())
        # create an empty dict
        output_dict = {}
        # check if there are repeated letters
        if repetitions.count(repetitions[0]) != len(repetitions):
            # if so, find the max value and the index where it's
            max_value = max(values)
            index = values.index(max_value)
            # create a dict with the key:value pair
            output_dict[val_dict[max_value]] = max_value
            # remove the letter and the value
            values.remove(max_value)
            keys.pop(index)
            # repeat the operation
            max_value = max(values)
            index = values.index(max_value)
            output_dict[val_dict[max_value]] = max_value
            # and so on
            while len(values) > 1:
                values.remove(max_value)
                keys.pop(index)
                max
