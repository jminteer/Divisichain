import sys
import FactorialDivider

if len(sys.argv) != 5:
    print("python3 GenTrans mode(0=normal,1=shift) from to amount")
    exit()

outstrt = "curl -H \"Content-type:application/json\" --data \'{\"data\" : \""
data = str(sys.argv[2]) + "," + str(sys.argv[3]) + ","
outend = "\"}\' http://localhost:3001/mineBlock"


if sys.argv[1] == str(0):
    data += sys.argv[4]
elif sys.argv[1] == str(1):
    data += str(1.0 * 10**(-1*int(sys.argv[4])))
else:
    data += str(FactorialDivider.main(int(sys.argv[4])))

outfile = open("trans.sh", "w")
outfile.write(outstrt + data + outend)

    
