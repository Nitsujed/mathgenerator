from .__init__ import *
from ..__init__ import Generator


def quotientofpowersamebaseFunc(maxBase=50, maxPower=10):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 - power2

    problem = "The Quotient of {base}^{power1} and {base}^{power2} = " \
              "{base}^({power1}-{power2}) = {base}^{step}".format(base=base,
                                                                  power1=power1,
                                                                  power2=power2,
                                                                  step=step)
    solution = str(base**step)
    return problem, solution


quotientOfPowerSameBase = Generator("Quotient of Powers with Same Base", 82,
                                    "6^4 / 6^2 = 6^(4-2) = 6^2", "36", quotientofpowersamebaseFunc)
