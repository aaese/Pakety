f = 'x.*sin(x)-cos(x)';
x=linspace(0,pi*4,100);
plot(x,eval(f),x,0*x,':'); grid on;
xlabel('x'); ylabel('y');
z=ginput(1);
[zr,fr]=fzero(f,z(1));
hold on;
plot(zr,fr,'r*',z(1),z(2), 'g*')
hold off;

