#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # Should this be length instead of magic number?
    #  (Originally 16)
    ht = HashTable(length)

    # for i in range(len(weights) - 1):
    #     hash_table_insert(ht, weights[i], i)
    
    # for weight in weights:
    #     index1 = hash_table_retrieve(ht, weight)
    #     # print(f"Index 1: {index1}")
    #     index2 = hash_table_retrieve(ht, limit-weight)
    #     # print(f"Index 2: {index2}")

    #     if index2 is not None:
    #         if index1 >= index2:
    #             return (index1, index2)
    #         else:
    #             return (index2, index1)
    
    # return None

    for i in range(len(weights)):
        val = hash_table_retrieve(ht, limit - weights[i])
        if val is not None:
            return (i, val)
        else:
            hash_table_insert(ht, weights[i], i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
