from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculate_freqs(self, address):
        pass


class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculate_freqs(self, address):
        file = open(address)
        n = file.readline().split()
        words = []
        for i in n:
            if i not in words:
                words.append(i)
        for i in range(0, len(words)):
            print(n.count(words[i]), " times ", words[i])


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculate_freqs(self, address):
        file = open(address)
        n = file.readline()
        dict_words = {}
        for word in n.split():
            dict_words[word] = dict_words.get(word, 0) + 1
        for key in dict_words:
            print("{} : {}".format(key, dict_words[key]))

# TEST PHASE


my_address = 'strange.txt'
print("\n")
print("**List application of lab work**")
print("\n")
list_file = ListCount(my_address)
list_file.calculate_freqs(my_address)

print("\n")
print("**Dictionary application of lab work**")
print("\n")
dict_file = DictCount(my_address)
dict_file.calculate_freqs(my_address)
