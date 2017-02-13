#coding=utf-8
#!/usr/bin/python
#字符表
mstr = 'abcdefghijklmnopqrstuvwxyz'
lengthM = len(mstr)#字符表长度

def caesar(strs,shift):#凯撒加密法，strs为明文，shift为移动位数
	newstrs = ''
	for x in strs:
		numX = mstr.index(x)#获得x字符在mstr中的位置
		numX = (numX + shift)%lengthM#将字符移动shift位
		newstrs = newstrs + mstr[numX]
	return newstrs
def encrypt(pT,key):#栅栏加密法，pT为明文，key为行数
	#key行的字符串数组
	array = [""]*key
	#将明文pT，按列写入array中
	for x in range(0,len(pT)):
		col = x%key
		#print col
		array[col] +=pT[x]
		#print array
	#cp为密文，将array按行读出
	cp =""
	for x in array:
		cp += x
	return cp
def decrypt(cp,key):#栅栏加密法解密，cp为密文，key为列数
	colN = (len(cp)-1)/key +1	#行数
	numL = key*colN - len(cp)
	#print "colN =",colN
	pt = ''	
	array = ['']*colN
	for x in range(0,len(cp)):
		col = x%colN
		#print row
		if len(array[col]) + numL >= key:#如果有某一列未被补满，则该列的行数-1
			local = (x-key+numL)%(colN-1)
				
		else :
			local = col
		#print local
		array[local] += cp[x]
		#print array
	for x in array:
		pt += x
	return pt
			
if __name__ == '__main__':
	#栅栏加密法
	
	plainTxt = '''Samsung's forthcoming Chromebook Pro, which the company introduced in partnership with Google at CES last month, appeared to be the latest contender in my search for the perfect premium Chromebook. For me, that means a high-resolution screen, excellent keyboard and trackpad, and a battery that lasts all day. I'm also looking for a well-designed machine, not the cheap, netbook-inspired computers that were the hallmark of earlier Chromebooks.'''
	cliperTxt = encrypt(plainTxt.decode("utf8"),key)
	print cliperTxt
	print decrypt(cliperTxt,10)
'''
	#caesar
	strs = raw_input("Input character sequence:")
	shift = input("Shift Number:")
	C = caesar(strs,shift)
	print("CliperText:",C)#获得密文
	print("PlainText:",caesar(C,int(shift)*(-1)))#解码密文
'''
