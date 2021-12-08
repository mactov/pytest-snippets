# from component import Component
# from subcomponent import SubComponent

# subc = SubComponent()
# c = Component(subc)
# print(c.method('toto'))

import slow

def slow_dataset():
    dataset = Dataset()
    return dataset.load_data()