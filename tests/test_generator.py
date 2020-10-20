from src.generator import DataFactor, DataPattern

class TestDataFactor:
    def test_product(self):
        factors = {
            'drink': ['coffee', 'beer'],
            'price': [300, 500],
        }
        df = DataFactor(factors)
        result = df.product()
        expected = [
            { 'drink': 'coffee', 'price': 300 },
            { 'drink': 'coffee', 'price': 500 },
            { 'drink': 'beer', 'price': 300 },
            { 'drink': 'beer', 'price': 500 }
        ]
        assert result == expected

class TestDataPattern:

    def test_generate_1(self):
        p = DataPattern()
        # menu factor
        factors = {
            'drink': ['coffee'],
        }
        p.add('menu', factors)
        # glass factor
        factors = {
            'size': ['large', 'small']
        }
        p.add('glass', factors)
        expected = [
            [{'menu': { 'drink': 'coffee' }}, {'glass': { 'size': 'large' }}],
            [{'menu': { 'drink': 'coffee' }}, {'glass': { 'size': 'small' }}],
        ]
        assert expected == p.generate()

    def test_generate_2(self):
        p = DataPattern()
        # menu factor
        factors = {
            'drink': ['coffee', 'coke'],
        }
        p.add('menu', factors)
        # glass factor
        factors = {
            'size': ['large', 'small']
        }
        p.add('glass', factors)
        expected = [
            [{'menu': { 'drink': 'coffee' }}, {'glass': { 'size': 'large' }}],
            [{'menu': { 'drink': 'coffee' }}, {'glass': { 'size': 'small' }}],
            [{'menu': { 'drink': 'coke' }}, {'glass': { 'size': 'large' }}],
            [{'menu': { 'drink': 'coke' }}, {'glass': { 'size': 'small' }}],
        ]
        assert expected == p.generate()

    def test_generate_3(self):
        p = DataPattern()
        # menu factor
        factors = {
            'drink': ['coffee'],
        }
        p.add('menu', factors)
        # glass factor
        factors = {
            'size': ['large']
        }
        p.add('glass', factors)
        # topping factor
        factors = {
            'lemon': [0, 1]
        }
        p.add('topping', factors)
        expected = [
            [{'menu': { 'drink': 'coffee' }}, {'glass': { 'size': 'large' }}, {'topping': {'lemon': 0}}],
            [{'menu': { 'drink': 'coffee' }}, {'glass': { 'size': 'large' }}, {'topping': {'lemon': 1}}]
        ]
        assert expected == p.generate()

    # def test_add(self):
    #     p = DataPattern()
    #     # menu factor
    #     factors = {
    #         'drink': ['coffee', 'beer'],
    #         'price': [300, 500],
    #     }
    #     p.add('menu', factors)
    #     # glass factor
    #     factors = {
    #         'size': ['large', 'small']
    #     }
    #     p.add('glass', factors)
    #     # topping factor
    #     factors = {
    #         'lemon': [0, 1]
    #     }
    #     p.add('topping', factors)

