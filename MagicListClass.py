from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


# warping the list class to add to add functionality of skipping boundary checks.
class MagicList(list):
    # Adding the option to get a cls_type in order to support initializing assigned types.
    def __init__(self, cls_type=None):
        super().__init__(self)
        self.cls_type = cls_type

    # In case that the given index is within the list range we will use the list default behavior.
    # Otherwise we will append the given value to the list.
    def __setitem__(self, key, value):
        if key < len(self):
            super().__setitem__(key, value)

        else:
            super().append(value)

    # In case that the given index is within the list range we will use the list default behavior.
    # Otherwise we will create new instance of the cls_type and append it to the list.
    def __getitem__(self, item):
        if item < len(self):
            return super().__getitem__(item)

        else:
            if self.cls_type:
                obj = Person()
                self.append(obj)
                return super().__getitem__(item)


# checking regular assertion
A = MagicList()
A[0] = 5
print(A)

# checking initializing assigned type assertion
A = MagicList(cls_type=Person)
A[0].age = 5
print(A)


