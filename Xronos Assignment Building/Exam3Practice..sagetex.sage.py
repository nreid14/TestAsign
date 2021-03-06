## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file Exam3Practice..sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_183 = Integer(183); _sage_const_188 = Integer(188); _sage_const_89 = Integer(89); _sage_const_113 = Integer(113); _sage_const_112 = Integer(112); _sage_const_111 = Integer(111); _sage_const_110 = Integer(110); _sage_const_80 = Integer(80); _sage_const_116 = Integer(116); _sage_const_82 = Integer(82); _sage_const_83 = Integer(83); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_108 = Integer(108); _sage_const_99 = Integer(99); _sage_const_100 = Integer(100); _sage_const_92 = Integer(92); _sage_const_91 = Integer(91); _sage_const_90 = Integer(90); _sage_const_101 = Integer(101); _sage_const_102 = Integer(102); _sage_const_103 = Integer(103); _sage_const_66 = Integer(66); _sage_const_67 = Integer(67); _sage_const_64 = Integer(64); _sage_const_65 = Integer(65); _sage_const_62 = Integer(62); _sage_const_63 = Integer(63); _sage_const_60 = Integer(60); _sage_const_132 = Integer(132); _sage_const_68 = Integer(68); _sage_const_69 = Integer(69); _sage_const_122 = Integer(122); _sage_const_123 = Integer(123); _sage_const_77 = Integer(77); _sage_const_76 = Integer(76); _sage_const_71 = Integer(71); _sage_const_70 = Integer(70); _sage_const_73 = Integer(73); _sage_const_72 = Integer(72); _sage_const_79 = Integer(79); _sage_const_78 = Integer(78); _sage_const_81 = Integer(81); _sage_const_200 = Integer(200); _sage_const_121 = Integer(121); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_150 = Integer(150); _sage_const_159 = Integer(159); _sage_const_75 = Integer(75); _sage_const_74 = Integer(74); _sage_const_120 = Integer(120); _sage_const_127 = Integer(127); _sage_const_59 = Integer(59); _sage_const_58 = Integer(58); _sage_const_57 = Integer(57); _sage_const_56 = Integer(56); _sage_const_55 = Integer(55); _sage_const_54 = Integer(54); _sage_const_53 = Integer(53); _sage_const_52 = Integer(52); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_142 = Integer(142); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_131 = Integer(131); _sage_const_130 = Integer(130); _sage_const_197 = Integer(197); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_133 = Integer(133); _sage_const_164 = Integer(164); _sage_const_61 = Integer(61)## This file (Exam3Practice..sagetex.sage) was *autogenerated* from Exam3Practice..tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('Exam3Practice.', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_1 
_st_.blockbegin()
try:

 #####Define default Sage variables.
 #Default function variables
 var('x,y,z,X,Y,Z')
 #Default function names
 var('f,g,h,dx,dy,dz,dh,df')
 #Default Wild cards
 w0 = SR.wild(_sage_const_0 )


 def RandInt(a,b):
     """ Returns a random integer in [`a`,`b`]. Note that `a` and `b` should be integers themselves to avoid unexpected behavior.
     """
     return QQ(randint(int(a),int(b)))
     # return choice(range(a,b+1))

 def NonZeroInt(b,c, avoid = [_sage_const_0 ]):
     """ Returns a random integer in [`b`,`c`] which is not in `av`.
         If `av` is not specified, defaults to a non-zero integer.
     """
     while True:
         a = RandInt(b,c)
         if a not in avoid:
             return a



 #
except:
 _st_.goboom(_sage_const_29 )
_st_.blockend()
_st_.current_tex_line = _sage_const_23 
_st_.blockbegin()
try:
 q1c1 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q1c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q1c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q1c4 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q1c5 = RandInt(_sage_const_0 ,_sage_const_1 )
 q1c6 = RandInt(_sage_const_0 ,_sage_const_1 )
 q1c7 = RandInt(_sage_const_1 -q1c6,_sage_const_1 )
 q1c8 = RandInt(_sage_const_1 -q1c5,_sage_const_1 )

 q1f1 = q1c5*(x - q1c1 - _sage_const_1 ) + _sage_const_1 
 q1f2 = q1c6*(x - q1c2 - _sage_const_1 ) + _sage_const_1 
 q1f3 = q1c7*(x - q1c3 - _sage_const_1 ) + _sage_const_1 
 q1f4 = q1c8*(x - q1c4 - _sage_const_1 ) + _sage_const_1 

 q1p = expand(q1f1*q1f2*q1f3*q1f4)

 q1ans1 = q1c5 + q1c6 + q1c7 + q1c8
 q1ans2 = q1c5*q1c1 + q1c6*q1c2 + q1c7*q1c3 + q1c8*q1c4

except:
 _st_.goboom(_sage_const_43 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.inline(_sage_const_0 , latex(q1p(x)))
except:
 _st_.goboom(_sage_const_48 )
try:
 _st_.current_tex_line = _sage_const_54 
 _st_.inline(_sage_const_1 , latex(q1ans1))
except:
 _st_.goboom(_sage_const_54 )
try:
 _st_.current_tex_line = _sage_const_57 
 _st_.inline(_sage_const_2 , latex(q1ans2))
except:
 _st_.goboom(_sage_const_57 )
try:
 _st_.current_tex_line = _sage_const_60 
 _st_.inline(_sage_const_3 , latex((q1f1*q1f2*q1f3*q1f4)(x)))
except:
 _st_.goboom(_sage_const_60 )
_st_.current_tex_line = _sage_const_66 
_st_.blockbegin()
try:
 q2c1 = RandInt(_sage_const_1 ,_sage_const_5 )

 q2f1 = x**_sage_const_4  - q2c1**_sage_const_4 

 q2ans1 = _sage_const_2 *(q2c1)**(_sage_const_1 /_sage_const_2 )
 q2ans2 = x**_sage_const_2  + q2c1**_sage_const_2 
 q2ans3 = x + q2c1
 q2ans4 = x - q2c1

except:
 _st_.goboom(_sage_const_76 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_4 , latex(q2f1(x)))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_5 , latex(-q2c1))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_6 , latex(q2c1))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_7 , latex(-q2c1))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_8 , latex(q2c1))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_108 
 _st_.inline(_sage_const_9 , latex(q2ans2))
except:
 _st_.goboom(_sage_const_108 )
try:
 _st_.current_tex_line = _sage_const_108 
 _st_.inline(_sage_const_10 , latex(q2ans3))
except:
 _st_.goboom(_sage_const_108 )
try:
 _st_.current_tex_line = _sage_const_108 
 _st_.inline(_sage_const_11 , latex(q2ans4))
except:
 _st_.goboom(_sage_const_108 )
_st_.current_tex_line = _sage_const_116 
_st_.blockbegin()
try:
 q3c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )

 q3f1 = x**_sage_const_3  - q3c1**_sage_const_3 

 q3ans1 = -q3c1 / _sage_const_2  - _sage_const_3 **(_sage_const_1 /_sage_const_2 )*(q3c1 / _sage_const_2 )*i
 q3ans2 = -q3c1 / _sage_const_2  + _sage_const_3 **(_sage_const_1 /_sage_const_2 )*(q3c1 / _sage_const_2 )*i

 q3ans3 = x**_sage_const_2  + q3c1*x + q3c1**_sage_const_2 
 q3ans4 = x - q3c1

except:
 _st_.goboom(_sage_const_127 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_12 , latex(q3f1(x)))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_13 , latex(q3c1))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_14 , latex(q3ans1))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_15 , latex(q3ans2))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_16 , latex(q3ans3))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_17 , latex(q3ans4))
except:
 _st_.goboom(_sage_const_159 )
_st_.current_tex_line = _sage_const_164 
_st_.blockbegin()
try:
 q4c1 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q4c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q4c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q4c4 = RandInt(-_sage_const_5 ,_sage_const_5 )
 q4c5 = NonZeroInt(-_sage_const_3 ,_sage_const_3 )
 q4c6 = NonZeroInt(-_sage_const_3 ,_sage_const_3 )
 q4c7 = NonZeroInt(-_sage_const_3 ,_sage_const_3 )
 q4c8 = NonZeroInt(-_sage_const_3 ,_sage_const_3 )

 q4f1 = q4c5*x - q4c1
 q4f2 = q4c6*x - q4c2
 q4f3 = q4c7*x - q4c3
 q4f4 = q4c8*x - q4c4

 q4p = expand(q4f1*q4f2*q4f3*q4f4)

 q4ans1 = q4c1/q4c5 + q4c2/q4c6 + q4c3/q4c7 + q4c4/q4c8
 __tmp__=var("x"); q4ans2 = symbolic_expression((q4f1*q4f2*q4f3*q4f4)(x)).function(x)
except:
 _st_.goboom(_sage_const_183 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_188 
 _st_.inline(_sage_const_18 , latex(q4p(x)))
except:
 _st_.goboom(_sage_const_188 )
try:
 _st_.current_tex_line = _sage_const_197 
 _st_.inline(_sage_const_19 , latex(q4ans1))
except:
 _st_.goboom(_sage_const_197 )
try:
 _st_.current_tex_line = _sage_const_200 
 _st_.inline(_sage_const_20 , latex(q4ans2(x)))
except:
 _st_.goboom(_sage_const_200 )
_st_.current_tex_line = _sage_const_1 
_st_.blockbegin()
try:

 #####Define default Sage variables.
 #Default function variables
 var('x,y,z,X,Y,Z')
 #Default function names
 var('f,g,h,dx,dy,dz,dh,df')
 #Default Wild cards
 w0 = SR.wild(_sage_const_0 )


 def RandInt(a,b):
     """ Returns a random integer in [`a`,`b`]. Note that `a` and `b` should be integers themselves to avoid unexpected behavior.
     """
     return QQ(randint(int(a),int(b)))
     # return choice(range(a,b+1))

 def NonZeroInt(b,c, avoid = [_sage_const_0 ]):
     """ Returns a random integer in [`b`,`c`] which is not in `av`.
         If `av` is not specified, defaults to a non-zero integer.
     """
     while True:
         a = RandInt(b,c)
         if a not in avoid:
             return a



 #
except:
 _st_.goboom(_sage_const_29 )
_st_.blockend()
_st_.current_tex_line = _sage_const_23 
_st_.blockbegin()
try:
 q5c1T = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 q5c1 = q5c1T / NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[-q5c1T,_sage_const_0 ,q5c1T])
 q5c2T = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 q5c2 = q5c2T / NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[-q5c2T,_sage_const_0 ,q5c2T])
 q5c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 q5c4 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 q5c5 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )


 q5v1 = [x**_sage_const_2 , x**_sage_const_3 , e**x, log(x), abs(x), x**(_sage_const_1 /_sage_const_2 )]
 q5p1 = RandInt(_sage_const_0 ,_sage_const_5 )
 q5f1 = q5v1[q5p1]

 q5f2 = q5c1*q5f1(q5c2*x-q5c3)+q5c4

 if q5c4 > _sage_const_0 :
     q5UDvec = ["Up","Down"]
 else:
     q5UDvec = ["Down","Up"]

 if q5c3 > _sage_const_0 :
     q5LRvec = ["Left", "Right"]
 else:
     q5LRvec = ["Right", "Left"]

 if q5c1 < _sage_const_0 :
     flipYT = " and is flipped"
     flipYF = ""
 else:
     flipYF = " and is flipped"
     flipYT = ""

 if q5c2 < _sage_const_0 :
     flipXT = " and is flipped"
     flipXF = ""
 else:
     flipXF = " and is flipped"
     flipXT = ""



except:
 _st_.goboom(_sage_const_65 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_68 
 _st_.inline(_sage_const_21 , latex(q5f1(x)))
except:
 _st_.goboom(_sage_const_68 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_22 , latex(q5c1))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_23 , latex(q5c2*x-q5c3))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_24 , latex(q5c4))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_25 , latex(q5f2(x)))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_26 , latex(abs(q5c2)))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_27 , latex(flipXT))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_77 
 _st_.inline(_sage_const_28 , latex(_sage_const_1 /abs(q5c2)))
except:
 _st_.goboom(_sage_const_77 )
try:
 _st_.current_tex_line = _sage_const_77 
 _st_.inline(_sage_const_29 , latex(flipXT))
except:
 _st_.goboom(_sage_const_77 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_30 , latex(abs(q5c2)))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_31 , latex(flipXF))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_79 
 _st_.inline(_sage_const_32 , latex(_sage_const_1 /abs(q5c2)))
except:
 _st_.goboom(_sage_const_79 )
try:
 _st_.current_tex_line = _sage_const_79 
 _st_.inline(_sage_const_33 , latex(flipXF))
except:
 _st_.goboom(_sage_const_79 )
try:
 _st_.current_tex_line = _sage_const_80 
 _st_.inline(_sage_const_34 , latex(abs(q5c1)))
except:
 _st_.goboom(_sage_const_80 )
try:
 _st_.current_tex_line = _sage_const_80 
 _st_.inline(_sage_const_35 , latex(flipYT))
except:
 _st_.goboom(_sage_const_80 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_36 , latex(_sage_const_1 /abs(q5c1)))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_37 , latex(flipYT))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_38 , latex(abs(q5c1)))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_39 , latex(flipYF))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_40 , latex(_sage_const_1 /abs(q5c1)))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_41 , latex(flipYF))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_42 , latex(q5UDvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_43 , latex(abs(q5c4)))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_90 
 _st_.inline(_sage_const_44 , latex(q5UDvec[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_90 )
try:
 _st_.current_tex_line = _sage_const_90 
 _st_.inline(_sage_const_45 , latex(abs(q5c4)))
except:
 _st_.goboom(_sage_const_90 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_46 , latex(q5LRvec[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_47 , latex(abs(q5c3)))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_48 , latex(q5LRvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_49 , latex(abs(q5c3)))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_50 , latex(_sage_const_1 /abs(q5c2)))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_51 , latex(flipXT))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_52 , latex(abs(q5c1)))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_53 , latex(flipYT))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_54 , latex(q5UDvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_55 , latex(abs(q5c4)))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_56 , latex(q5LRvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_57 , latex(abs(q5c3)))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_58 , latex(_sage_const_1 /abs(q5c2)))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_59 , latex(flipXT))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_60 , latex(abs(q5c1)))
except:
 _st_.goboom(_sage_const_111 )
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_61 , latex(flipYT))
except:
 _st_.goboom(_sage_const_111 )
try:
 _st_.current_tex_line = _sage_const_112 
 _st_.inline(_sage_const_62 , latex(q5UDvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_112 )
try:
 _st_.current_tex_line = _sage_const_112 
 _st_.inline(_sage_const_63 , latex(abs(q5c4)))
except:
 _st_.goboom(_sage_const_112 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_64 , latex(q5LRvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_65 , latex(abs(q5c3)))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_66 , latex(_sage_const_1 /abs(q5c2)))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_67 , latex(flipXT))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_68 , latex(abs(q5c1)))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_69 , latex(flipYT))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_70 , latex(q5UDvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_71 , latex(abs(q5c4)))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_72 , latex(q5LRvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_73 , latex(abs(q5c3)))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_74 , latex(_sage_const_1 /abs(q5c2)))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_75 , latex(flipXT))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_131 
 _st_.inline(_sage_const_76 , latex(abs(q5c1)))
except:
 _st_.goboom(_sage_const_131 )
try:
 _st_.current_tex_line = _sage_const_131 
 _st_.inline(_sage_const_77 , latex(flipYT))
except:
 _st_.goboom(_sage_const_131 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_78 , latex(q5UDvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_79 , latex(abs(q5c4)))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_133 
 _st_.inline(_sage_const_80 , latex(q5LRvec[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_133 )
try:
 _st_.current_tex_line = _sage_const_133 
 _st_.inline(_sage_const_81 , latex(abs(q5c3)))
except:
 _st_.goboom(_sage_const_133 )
_st_.endofdoc()

