class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count = 0

    def __iter__(self):
        return self


    def __next__(self):
        item = sum(self.list_of_list, [])
        if len(item) == self.count:
            raise StopIteration
        else:
            self.count += 1
            return item[self.count - 1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
