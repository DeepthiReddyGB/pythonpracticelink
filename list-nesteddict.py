num_list = [1, 2, 3, 4, 5]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)