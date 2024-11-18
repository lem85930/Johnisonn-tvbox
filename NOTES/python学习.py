[24-11-18]:

1.sorted()函数用法、lambda匿名函数用法:

(1)
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  

(2)
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words,reverse=True)
print(sorted_words)  

(3)
points = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_points = sorted(points, key=lambda x: x[1])  # 基于每个元组的第二个元素排序
print(sorted_points)  

(4)
my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_keys = sorted(my_dict.keys())
print(sorted_keys)  