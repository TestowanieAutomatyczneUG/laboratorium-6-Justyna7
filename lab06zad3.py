import unittest


class Piosenka:
    def __init__(self):
        self.song = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\
\nOn the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens,\
 two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings,\
 four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, \
six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, \
seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, \
two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, \
eight Maids-a-Milking,seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, \
nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, \
four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, \
ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, \
five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

    def change(self, x):
        if x > 0:
            return x - 1
        return x

    def wyswietl(self, n, m=None):
        if m is not None and isinstance(n, int) and isinstance(m, int):
            if n > 12 or n < -12 or n == 0 or m > 12 or m < -12:
                raise Exception
            else:
                s = self.song.split('\n')
                a = self.change(n)
                b = self.change(m)
                w = ""
                if m == 0:
                    s2 = s[a:]
                else:
                    s2 = s[a:b]
                for i, x in enumerate(s2):
                    if i != 0:
                        w = w + '\n' + x
                    else:
                        w = w + x

                return w
        else:
            if m is not None:
                raise Exception
            if isinstance(n, str):
                if n == "ALL":
                    return self.song
                else:
                    raise Exception
            elif isinstance(n, int):
                if n > 12 or n < -12 or n == 0:
                    raise Exception
                else:
                    s = self.song.split('\n')
                    a = self.change(n)
                    return s[a]
            else:
                raise Exception


class PiosenkaTest(unittest.TestCase):

    def setUp(self):
        self.temp = Piosenka()

    def test1(self):
        self.assertEqual(self.temp.wyswietl(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test4(self):
        self.assertEqual(self.temp.wyswietl(4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_6(self):
        self.assertEqual(self.temp.wyswietl(-6), "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test1and3(self):
        self.assertEqual(self.temp.wyswietl(1, 3), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\
\nOn the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test8and0(self):
        self.assertEqual(self.temp.wyswietl(8, 0), "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, \
six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, \
seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, \
two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, \
eight Maids-a-Milking,seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, \
nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, \
four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, \
ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, \
five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def testall(self):
        self.assertEqual(self.temp.wyswietl("ALL"), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\
\nOn the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens,\
 two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings,\
 four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, \
six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, \
seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, \
two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, \
eight Maids-a-Milking,seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, \
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, \
nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, \
four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\
\nOn the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, \
ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, \
five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_Exceptions30(self):
        self.assertRaises(Exception, self.temp.wyswietl, 30)

    def test_Exceptions_27(self):
        self.assertRaises(Exception, self.temp.wyswietl, -27)

    def test_Exceptions0(self):
        self.assertRaises(Exception, self.temp.wyswietl, 0)

    def test_Exceptionsand3(self):
        self.assertRaises(Exception, self.temp.wyswietl, 0, 3)

    def test_Exceptionstab(self):
        self.assertRaises(Exception, self.temp.wyswietl, [30])

    def test_Exceptionsdict(self):
        self.assertRaises(Exception, self.temp.wyswietl, {})

    def test_Exceptionsstr(self):
        self.assertRaises(Exception, self.temp.wyswietl, "blah")

    def test_Exceptions30and0(self):
        self.assertRaises(Exception, self.temp.wyswietl, 30, 0)

    def test_Exceptions0_20(self):
        self.assertRaises(Exception, self.temp.wyswietl, 0, -20)

    def test_Exceptions3anddict(self):
        self.assertRaises(Exception, self.temp.wyswietl, 3, {})

    def tearDown(self):
        self.temp = None