%%Free Vibration Responce of a SDOF Damped System
clc;
clear all;
m=25;
k=25;
c=18;
global m k c
dt = 0.05;
t=0:dt:50;
y0=[0.05 0];%%[velocity disp]
[tsol,ysol]=ode45('testode2',[0:dt:50],y0);%%ODE-matlab fun for 
damping_ratio=c/(2*sqrt(k*m))
if damping_ratio < 1
    disp('The system is underdamped')
end
if damping_ratio == 1
    disp('The system is critically damped')
end
if damping_ratio > 1
    disp('The system is overdamped')
end
plot(t,ysol(:,2))
title('Displacement V/s Time')
xlabel('Time') 
ylabel('Displacement') 
grid on
figure
plot(t,ysol(:,1))
title('Velocity V/s Time ')
xlabel('Time') 
ylabel('Velocity') 
grid on



