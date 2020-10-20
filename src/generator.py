import itertools


class DataFactor(object):
    factors = {}

    def __init__(self, factors):
        self.factors = factors

    def product(self):
        product_values = [x for x in itertools.product(*self.factors.values())]
        result = [dict(zip(self.factors.keys(), v)) for v in product_values]
        return result


class DataPattern(object):
    patterns = {}

    def add(self, name, factors):
        self.patterns[name] = DataFactor(factors)

    def generate(self):
        dict_pattern = []
        for name, factors in self.patterns.items():
            # result = []
            # for f in factors:
            #     result.append(dict(zip([name], [f])))
            dict_factors = [dict(zip([name], [f])) for f in factors.product()]
            dict_pattern.append(dict_factors)

        result = self.product(dict_pattern)
        return result

    def product(self, args):
        if len(args) == 2:
            # result = []
            # for x in args[0]:
            #     for y in args[1]:
            #         result.append([x] + [y])
            result = [[x] + [y] for x in args[0] for y in args[1]]
            return result
        else:
            sub = args.pop(0)
            sub_product = self.product(args)
            result = [[s] + p for s in sub for p in sub_product]
            return result
