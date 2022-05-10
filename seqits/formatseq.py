import argparse
from colorama import Fore,init
init(autoreset=True)
parser = argparse.ArgumentParser(description="Seqits search tool")
parser.add_argument('input', 
                    help='input raw fasta file')
parser.add_argument('-n','--num', 
                    type=int,
                    default=60,
                    help='number of characters per line')
parser.add_argument('-o','--out',
                    default='output.fa',
                    help='output file')
parser.add_argument('-s','--show', 
                    default='false',
                    help='true/false, show the output on the screen')
args = parser.parse_args()
filename=args.input
print('Waiting for formatting ...')
with open(filename) as f:
    file=f.read()
remove_list=['\r','\t',' ','\n','\b']
s=''
for i in file.split('>')[1:]:
    temp=i.split('\n')
    n=0
    s+='>'+temp[0]+'\n'
    for j in ''.join(temp[1:]):
        if j not in remove_list:
            s+=j.upper()
            n+=1
            if n%args.num==0:
                s+='\n'        
    if n%args.num!=0:
        s+='\n'
if args.show=='true':
    print(s)
elif args.show!='false':
    print(Fore.RED+'show mode error!')
    exit(0)
if args.out:
    with open(args.out,'w') as f:
        f.write(s)
    print(Fore.GREEN+'saved to "'+args.out +'" successfully.')