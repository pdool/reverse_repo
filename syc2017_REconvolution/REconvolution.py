import string
import pdb
dic = string.printable

data = [0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x7B, 0x7C, 0x7D, 0x7E]
# print len(data)
# print chr(data[-1])

key = [0x72, 0xE9, 0x4D, 0xAC, 0xC1, 0xD0, 0x24, 0x6B, 0xB2, 0xF5, 0xFD, 0x45, 0x49, 0x94, 0xDC, 0x10, 0x10, 0x6B, 0xA3, 0xFB, 0x5C, 0x13, 0x17, 0xE4, 0x67, 0xFE, 0x72, 0xA1, 0xC7, 0x4, 0x2B, 0xC2, 0x9D, 0x3F, 0xA7, 0x6C, 0xE7, 0xD0, 0x90, 0x71, 0x36, 0xB3, 0xAB, 0x67, 0xBF, 0x60, 0x30, 0x3E, 0x78, 0xCD, 0x6D, 0x35, 0xC8, 0x55, 0xFF, 0xC0, 0x95, 0x62, 0xE6, 0xBB, 0x57, 0x34, 0x29, 0x0E]
# print len(key)
# print hex(key[0x20])
# print len(key) - len(data) + 1
# key[i] = (ans[0] ^ data[i]) + (ans[1] ^ data[i - 1]) + (ans[2] ^ data[i -2]) + ... + (ans[i] ^ data[0])

ans = chr(0x21 ^ 0x72)

def func(ans, n):
	# if n == 32:
		# pdb.set_trace()
	sum = 0
	for i in range(n + 1):
		sum += (ord(ans[i]) ^ data[n - i])
		
	# print int(hex(sum)[-2:], 16)
	return int(hex(sum)[-2:], 16)



for i in xrange(1, 35):
	try:
                print ans
		for j in dic:
			# if i == 32:
				# pdb.set_trace()
			# if j == 'C':
				# pdb.set_trace()
			if func(ans + j, i) == key[i]:
				ans += j
				#  print ans
				break
	except:
		break
	
