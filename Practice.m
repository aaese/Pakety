A = rand(20);
b = eig(A);
b = sort(b);

B=rand(4);
[V,D]= eig(B);
B*V;
V*D;

n=5;
X=zeros(n);
X(1,n)=1;
X(n,1)=1;
X-2*diag(ones(1,n))+diag((ones(1,n-1)),1)+diag((ones(1,n-1)),-1);

M=rand(8)
max(M)
max(M')
max(max(M))
[m, n]=find(M > 0.2);
C=[m,n]

