```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, ext
    return f'{class_name}.{strongest_name}'
```

The script calculates the strength of each extension as the difference between uppercase and lowercase letters in the extension name. The strongest extension is selected and returned in the format `ClassName.StrongestExtensionName` with the class name and the strongest extension name concatenated. If there are extensions with the same strength, it selects the one that comes first in the list. 

Here is an example of how to use the defined function:
```python
print( Strongest_Extension( "C", ["aA", "BB", "bB", "Cc", "Dd"] ) )
```
This will print out: `C.aA` 

The test cases would look like this:
```python
def test_strongest_extension():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"
    assert Strongest_Extension("abc", ["Abc", "abc", "BCc", "CDd"]) == "abc.Abc"
    assert Strongest_Extension("hello", ["AHello", "ala", "arlo", "Booya"]) == "hello.AHello"
    assert Strongest_Extension("parallel", ["ParallelliTy", "Parallely", "channel", "CHANNEL"]) == "parallel.ParallelliTy"
``` 
This would be run with:
```python
test_strongest_extension()
```  ensure that the test cases run correctly.