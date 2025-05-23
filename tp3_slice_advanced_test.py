import io
import unittest.mock
import slice_advanced as ex3


class TP3SliceAdvancedTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_slice_advanced(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="Hello, World!"):
            ex3.slice_advanced()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "o ol!")
        with unittest.mock.patch('builtins.input', return_value="12345678910"):
            ex3.slice_advanced()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[1], "5790")

if __name__ == '__main__':
    unittest.main()

    x = "Awesome"
    x_real = x.lower()

    print(x_real[ :3])    #Imprime las 3 primera letras del texto

    mitad = int(len(x_real)/2)      #me dice cual es la mitad del texto // El int me quita la parte fraccional, no redondea
    print(x_real[mitad - 1 : mitad + 2])      #DESDE mitad-2 HASTA mitad+1

    print(x_real[ :4] + x[-3: ])
