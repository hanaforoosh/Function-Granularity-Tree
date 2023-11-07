from itertools import chain, combinations


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.is_tepid = False
        self.invocation_distance = 0

    def __getitem__(self, key):
        for child in self.children:
            if child.name == key:
                return child
        raise KeyError(f"Child node '{key}' not found.")

    def __setitem__(self, key, value):
        for child in self.children:
            if child.name == key:
                child = value
                return
        new_child = value
        new_child.parent = self
        self.children.append(new_child)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def get_nearest_tepid(self, name):
        """
        get_nearest_tepid(node)
        """
        found_node = self.find(name)
        if found_node:
            return found_node
        else:
            return 'Noooo'


    def run_on(self, function_node ,runner_node):
        """
        get_nearest_tepid(node)
        """

    def config(self, tepid_nodes: list = None) -> list:
        """
        set config
        """

    def reconfig(self) -> list:
        """
        set reconfig
        """

    def print_tree(self, num_of_space=2):
        print(self.name)
        fix_part = "├" + 4 * "─"
        for child in self.children:
            print(num_of_space * " ", end="")
            print(fix_part, end=" ")
            new_number_of_space = num_of_space + len(fix_part) + (len(str(self.name)))
            child.print_tree(new_number_of_space)

    def find(self, name):
        result = []
        if self.name == name:
            result.append(self)
            return result
        else:
            for child in self.children:
                found = child.find(name)
                result += found

            return result

    ######### Optionals #########
    def get_tepids(self):
        """
        get_tepids
        """

    def reset(self, reset_tepids=True):
        """
        reset
        """

    def print_tepids(self):
        """
        print_tepids
        """


# this function make powerset of a given set
def get_powerset(in_set):
    # Convert the input set to a list
    in_list = list(in_set)
    # Generate all possible subsets using combinations from itertools
    subsets = chain.from_iterable(
        combinations(in_list, r) for r in range(len(in_list) + 1)
    )
    # Convert each subset to a set
    powerset = [set(subset) for subset in subsets]
    powerset.remove(in_set)

    powerset.remove(set())
    return powerset


def make_tree(data):
    root = TreeNode("Alpine")
    for k, v in data.items():
        node_k = TreeNode(k)
        root[node_k.name] = node_k

    for k, v in data.items():
        for pack in v:
            if len(pack) == 1:
                root[k][pack] = TreeNode(pack)

    for k, v in data.items():
        # v is python for example
        length = 1
        exist = True
        while exist == True:
            exist = False
            for packs in v:
                if len(packs) == length:
                    exist = True

                    powerset = get_powerset(packs)
                    for p in powerset:
                        found_list = root.find(p)

                        for found in found_list:
                            if found is not None and len(found.name) == len(packs) - 1:
                                found[packs] = TreeNode(packs)

            length += 1
    return root


# for k,v in data.items():
#     # v is python for example
#     for packs in v:
#         root[k][v] = TreeNode(packs)

if __name__ == "__main__":
    data = {
        "python": [
            frozenset({"pyspark", "flask"}),
            frozenset({"numpy"}),
            frozenset({"hh"}),
            frozenset({"hh", "flask"}),
            frozenset({"pandas"}),
            frozenset({"numpy", "flask"}),
            frozenset({"numpy", "pyspark", "flask"}),
            frozenset({"numpy", "pyspark"}),
            frozenset({"pyspark"}),
            frozenset({"flask"}),
        ],
        "nodejs": [frozenset({"nnn"})],
        "java": [],
    }
    root = make_tree(data)
    # root.print_tree()
    found =root.get_nearest_tepid(frozenset({'pyspark', 'flask', 'numpy'}))
    print('I Found this:',found)