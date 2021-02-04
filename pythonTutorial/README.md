# Python Tips & Tricks

## Argument parsing

When parsing arguments into the python interpreter, we can access the argument information with the `sys` module.

**Calling python with no arguments**
```bash
$> python 
Python 3.9.1 (default, Jan  8 2021, 17:17:43)
[Clang 12.0.0 (clang-1200.0.32.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.argv[0]
''
```

**Calling a python script interactively**
```bash
$> python -i example.py
2 is a prime number
3 is a prime number
4 equals 2 * 2
...
9 equals 3 * 3
>>> import sys
>>> sys.argv
['example.py']
```

**Calling a python script as a module**
```bash
$> python -i -m example
2 is a prime number
3 is a prime number
4 equals 2 * 2
...
9 equals 3 * 3
>>> import sys
>>> sys.argv
['/Users/alfredang/Code/tis-but-a-scratch/pythonTutorial/ch2_interpreter/example.py']
```

## Default function arguments

When a default value is specified for a function argument, it is only evaluated once. This might cause issues when the value required is mutable (lists/dictionary/class instances).

```python
def gimmeAdd(x, acc=[]):
  acc.append(x)
  return acc

print(gimmeAdd(1))
print(gimmeAdd(2))
print(gimmeAdd(3))
```

The above snippet yields:

```Python
[1]
[1,2]
[1,2,3]
```

However, if we want a fresh instance of an empty list each time `gimmeAdd` is called, we instantiate `acc` with `None` instead.

```python
def gimmeAdd2(x, acc=None):
  if acc is None:
    acc = []
  acc.append(x)
  return acc

print(gimmeAdd2(1))
print(gimmeAdd2(2))
print(gimmeAdd2(3))
```

Running this new version yields:
```python
[1]
[2]
[3]
```
