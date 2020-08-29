# -*- coding: UTF-8 -*-
#Write Sampe text

text = open('data/text/sample.txt', mode='w')
text.write('A	B	C	 D 	E	F	G	H	I\n')
text.write('A22197459	20200630	 300,000 	200630155109 	20200701	6858501133	001	A\n')
text.write('A22197316	20200630	 166,000 	200630141926 	20200701	6858501133	001	A\n')
text.write('A22197154	20200630	 299,600 	200630122520 	20200701	6858501133	001	A\n')

text.close()