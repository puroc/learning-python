#########################
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)


#########################
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)


"""迭代器和生成器
迭代器是每次可以返回一个对象元素的对象，例如返回一个列表。我们到目前为止使用的很多内置函数（例如 enumerate）都会返回一个迭代器。

迭代器是一种表示数据流的对象。这与列表不同，列表是可迭代对象，但不是迭代器，因为它不是数据流。

生成器是使用函数创建迭代器的简单方式。也可以使用类定义迭代器，更多详情请参阅此处。

下面是一个叫做 my_range 的生成器函数，它会生成一个从 0 到 (x - 1) 的数字流。"""

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
"""注意，该函数使用了 yield 而不是关键字 return。这样使函数能够一次返回一个值，并且每次被调用时都从停下的位置继续。关键字 yield 是将生成器与普通函数区分开来的依据。

注意，因为这段代码会返回一个迭代器，因此我们可以将其转换为列表或用 for 循环遍历它，以查看其内容。例如，下面的代码："""

for x in my_range(5):
    print(x)