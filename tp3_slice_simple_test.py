import io
import unittest.mock
import slice_simple as ex2

class TP3SliceSimpleTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_slice_simple(self, mock_stdout):
        ex2.slice_simple()
        results = mock_stdout.getvalue().splitlines()

        # Matias should contain A and I
        self.assertEqual(results[0], "awe")
        self.assertEqual(results[1], "eso")
        self.assertEqual(results[2], "awesome")

if __name__ == '__main__':
    unittest.main()

    x = "Awesome"
    x_real = x.lower()

    print(x_real[ :3])    #Imprime las 3 primera letras del texto

    mitad = int(len(x_real)/2)      #me dice cual es la mitad del texto // El int me quita la parte fraccional, no redondea
    print(x_real[mitad - 1 : mitad + 2])      #DESDE mitad-2 HASTA mitad+1

    print(x_real[ :4] + x[-3: ])
