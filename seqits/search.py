import argparse
from colorama import Fore,init
init(autoreset=True)
parser = argparse.ArgumentParser(description="Seqits search tool")
parser.add_argument('input', 
                    help='input raw fasta file')
parser.add_argument('gene', 
                    help='input gene(s)')
parser.add_argument('-t','--type', 
                    default='string',
                    help='string/file, type of input gene(s). For file, one gene one line; for string, gene(s) seperate with \',\'')
parser.add_argument('-m','--mode', 
                    default='fast',
                    help='fast/order, "fast" mode may faster than "order" mode, but "order" mode can show your output accoring to the order your gene(s) input')
parser.add_argument('-o','--out',
                    default='output.fa',
                    help='output file')
parser.add_argument('-s','--show', 
                    default='false',
                    help='true/false, show the output on the screen')
args = parser.parse_args()
filename=args.input
gene_list=args.gene
gene_type=args.type
if gene_type=='string':
    gene_list=args.gene.split(',')
elif gene_type=='file':
    with open(args.gene) as f:
        gene_list=f.readlines()
        exit(0)
else:
    print(Fore.RED+'type of input gene(s) error!')
    exit(0)
if '' in gene_list:
    gene_list.remove('')
with open(filename) as f:
    file=f.read()
s=''
if args.mode=='fast':
    for i in file.split('>')[1:]:
        temp=i.split('\n')
        if temp[0].split(' ')[0] in gene_list:
            s+='>'+temp[0]+'\n'+'\n'.join(temp[1:])
elif args.mode=='order':
    for i in gene_list:
        for j in file.split('>')[1:]:
            temp=j.split('\n')
            if temp[0].split(' ')[0]==i:
                s+='>'+temp[0]+'\n'+'\n'.join(temp[1:])
                break
else:
    print(Fore.RED+'search mode error!')
    exit(0)
if args.show=='true':
    print(s)
elif args.show!='false':
    print(Fore.RED+'show mode error!')
    exit(0)
if args.out:
    with open(args.out,'w') as f:
        f.write(s)
    print(Fore.GREEN+'saved to "'+args.out +'" successfully.')