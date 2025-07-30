def multiply(x, y):
    return x * y

def self_math(func):
    def inner_func(x):
        return func(x, x)
    
    return inner_func

square = self_math(multiply)

print(multiply(5,5))
print(square(5))
print(square(8))
print(square(9))