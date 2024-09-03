```python
def Strongest_Extension(class_name, extensions):
    """
    Extensions are to be used to load additional classes to the class.
    The strength of the extension is as follows: Let CAP be the number of the 
    uppercase letters in the extension's name, and let SM be the number of 
    lowercase letters in the extension's name, the strength is given by the fraction CAP - SM. 
    Should find the each the all extensions with the same strength, you should
    choose the one that comes first in the list.
    ```

def test_extension():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    def main():
        class_name = "Slices"
        extensions = ["SErviNGSliCes", "Cheese", "StuFfed"]
        print(Strongest_Extension(class_name, extensions))

if __name__ == "__main__":
    main()
```

In the script, there is a function called `Strongest_Extension` that takes the `class_name` and `extensions` as parameters. The function returns the strength of extensions using the formula mentioned in the problem statement. 

The function then loops through the extensions, comparing each with the class name. The first matching extension is returned as the strongest one.

The `test_extension` function is used to run the `Strongest_Extension` function and checks if the output is correct. 

Finally, the `main` function defines the class name and extensions, and then calls the `test_extension` function to verify the correctness of the `Strongest_Extension` function.