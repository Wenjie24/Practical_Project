def num_vowels(text):
    total = 0
    trigger = ['a','e','i','o','u']
    for i in text:
        if i.lower() in trigger:
            total += 1
    return total

print(num_vowels('hello'))
