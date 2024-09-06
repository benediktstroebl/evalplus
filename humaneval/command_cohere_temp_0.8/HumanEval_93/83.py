```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.lower() if char.lower() not in vowels else chr(ord(swapped.lower()) + (97 + (ord(vowels.find(char.lower())) + 1) % 26) % 26)
```

To test the function, it is important to have test cases that cover different scenarios, including edge cases and expectations. Here is an example:
```python
def test_encode():
    # Lowercase vowels and expectations
    assert encode('hello') == 'hELLO'
    assert encode('world') == 'wrld'
    
    # Uppercase vowels and expectations
    assert encode('Hello') == 'hELLO'
    assert encode('World') == 'wrld'
    
    # Mixed case vowels and expectations
    assert encode('Happy') == 'hPPY'
    assert encode('Love') == 'lVve'
    
    # No vowel scenarios
    assert encode('xyz') == 'xyz'
    assert encode('typos') == 'tYPOS'
    
    # Multiple vowels scenarios
    assert encode('hello world') == 'hELLO wrld'
    assert encode('Love story') == 'lVve stry'
```

This test suite will ensure that the encode function behaves as expected with different cases of vowels, mixed case scenarios, and scenarios with no vowels or multiple vowels. 

It is important to make sure that test cases cover different aspects of the function's behavior, such as edge cases and expected behavior. This will help ensure that the function is fully tested and behaves as expected. 

As a language model, I cannot run the script but if you would like to execute it in a Python environment, it will output the results of the encode function according to the test cases provided.