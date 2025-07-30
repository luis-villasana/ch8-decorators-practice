def multiply(x, y):
    return x * y

def self_math(func):
    def inner_func(x):
        return func(x, x)
    
    return inner_func

square = self_math(multiply)

print(multiply(5, 5)) # 25
print(square(5)) # 25

print(multiply(6, 6)) # 36
print(square(6)) # 36

print(multiply(10, 10)) # 100
print(square(10)) # 100