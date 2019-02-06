from typeguard import typechecked


def greeting(name: str) -> str:
    return 'Hello ' + name


print(greeting('Igor'))


def car(kg: int = 1) -> int:
    return 'kg' + str(kg)


print(car())


class Cat:
    size: int = 100

    def __init__(self, size: int):
        self.size = size


def food(meat: Cat) -> None:
    print('size: ' + str(meat.size))


cat = Cat(20)
number = 123

food(cat)



@typechecked
def car(kg: int) -> int:
    return 'kg' + str(kg)


print(car(100))
