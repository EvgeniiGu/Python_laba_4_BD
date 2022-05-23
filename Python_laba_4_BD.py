#99 13 2 67 14 89 23 45 128 1 34 18 88 78 253 6 531 236 778 16 4 9
import random
class Search_tree:
    _adress_space = random.sample(range(0, 200), 30)
    _order_of_addresses = []
    _tree = {}
    _first_cell = None
    _last_cell = None
    def __init__(self, list_of_elements):
        sorted_list = self._sort(list_of_elements)
        self._tree = self._save(sorted_list)
    def _sort(self, list_of_elements):
        iter = 0
        flag = 0
        while True:
            if list_of_elements[iter] > list_of_elements[iter+1]:
                temp = list_of_elements[iter]
                list_of_elements[iter] = list_of_elements[iter+1]
                list_of_elements[iter+1] = temp
            elif list_of_elements[iter] < list_of_elements[iter+1]:
                flag += 1
            else:
                print("err")
            if iter == len(list_of_elements)-2:
                iter = 0
                if flag == len(list_of_elements)-1:
                    break
                else:
                    flag = 0
            else:
                iter+=1
        return list_of_elements
    def _save(self, sorted_list):
        temp_dict = {x: [None, None, None] for x in self._adress_space}
        for j in temp_dict:
            if temp_dict[j][0] == None:
                current_cell = j
                break
        self._first_cell = current_cell
        right_cell = None
        left_cell = None
        next_cell = None
        previous_cell = None
        for elem in sorted_list:
            for j in temp_dict:
                if temp_dict[j][0] == None and j != current_cell:
                    next_cell = j
                    break
            if sorted_list[len(sorted_list)-1] == elem:
                next_cell = None
                self._last_cell = current_cell
            temp_dict[current_cell] = [elem, right_cell, left_cell]
            self._order_of_addresses.append(current_cell)
            right_cell = next_cell
            left_cell = previous_cell
            previous_cell = current_cell
            current_cell = next_cell
        return temp_dict
    def _print_search_tree(self):
        tree_keys = list(self._tree.keys())
        search_tree = []
        flag = True if len(tree_keys)%2!=0 else False
        print(flag)
        for i in tree_keys:
            print(self._tree[i])
    def direct_bypass(self):
        pass
    def insert_element(self):
        pass
    def delete_element(self):
        pass
    def view(self):
        pass

if __name__ == "__main__":
    f = Search_tree(list(map(int, input().split())))
    print(f._tree)
    #print(f._order_of_addresses)