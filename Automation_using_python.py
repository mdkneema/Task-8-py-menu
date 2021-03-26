import os
import getpass
import pyfiglet
os.system("clear")
os.system('tput blink')
os.system('tput setaf 2')
print(pyfiglet.figlet_format("FSOCIETY"))
os.system('tput sgr0')
os.system('tput setaf 7')
print("Please Enter Fsociety Pass \n")
pas = getpass.getpass()
if(pas == "123"):
    while True :

        print('''\n --------Friday Automation manager--------
        c:clear e:Exit the Program
        1.Linux Basic(LVM)
        2.Docker
        4.Hadoop
        5.AWS
        ''')
        print("Enter Your option : ",end="")
        command = input()
        if(command == "1"):
            while True :

                print('''\n --------LVM manager--------
                c:clear e:Back to main menu
                1.Show avialble devices/HDD
                2.create Physical Volumes(PV)
                3.Create Volume Group (VG)
                4.Extend Volume Group
                5.Create Logical Volume (LV)
                6.Extend LV
                7.Show physical volumes
                8.Show volume groups
                9.show LVM
                10.List of HDD blocks
                11.Mount LVM's
                ''')
                print("Enter Your option : ",end="")
                command = input()
            
                if(command == "1"):
                    os.system("fdisk -l")
                elif(command == "c"):
                    os.system("clear")
                elif(command == "2"):
                    print("Enter device name :",end="")
                    pv = input()
                    os.system("pvcreate "+pv)
            
                elif(command == "3"):
                    print("Enter volume group name : ",end="")
                    name =input()
                    print("Enter device name you want in LVM : ",end="")
                    dev1 = input()
                    os.system("vgcreate {} {} ".format(name,dev1))
                elif(command == "4"):
                    print("Enter your new HDD name : ",end="")
                    hdd = input()
                    print("Enter your VG name : ",end="")
                    vgname = input()
                    os.system("vgextend {} {}".format(vgname,hdd))
            
                elif(command == "5"):
                    print("How much size do you want[Ex.5G] : ",end="")
                    size = input()
                    print("Enter your Volume group name : ",end="")
                    vgname =input()
                    print("Enter name for LVM : ",end="")
                    lvmname = input()
                    os.system("lvcreate -L {} -n {} {}".format(size,lvmname,vgname))
            
                elif(command =="6"):
                    print("Enter How much size do you wan to increase in GB [ex.5] : ",end="")
                    size=input()
                    print("Enter LVM device name : ",end="")
                    lvm = input()
                    os.system("lvextend --size +{}G {}".format(size,lvm))
                    os.system("resize2fs {}".format(lvm))

                elif(command == "7"):
                    os.system("pvdisplay")
            
                elif(command =="8"):
                    os.system("vgdisplay")

                elif(command == "9"):
                    os.system("lvs")

                elif(command == "10"):
                    os.system("lsblk")
            
                elif(command == "11"):
                    print("Enter device name that will mount : ",end="")
                    mountname = input()
                    print("Enetr mount point : ",end="")
                    point = input()
                    os.system("mount {} {}".format(mountname,point))
                elif(command =="e"):
                    os.system("clear")
                    break
        elif(command == "c"):
            os.system("clear")
        elif(command == "e"):
            break
        elif(command == "2"):
             while True :

                print('''\n --------Docker manager--------
                c:clear e:Back to main menu
                install docker : to install docker
                
                1.Display Images
                2.Pull images
                3.Display Container's
                4.Launch Container
                5.Start Container
                6.attach container
                7.stop Container
                8.Remove Container
                9.Remove Image
                
                start: To start docker service
                ''')
                print("Enter Your option : ",end="")
                command = input()
                if(command == "1"):
                    os.system("docker images")
                elif(command == "install docker"):
                    os.system("yum install docker-ce --nobest")
                elif(command == "c"):
                    os.system("clear")
                elif(command == "e"):
                    os.system("clear")
                    break
                elif(command == "2"):
                    print("Enter image you want to Download : ",end="")
                    image=input()
                    os.system("docker pull {}".format(image))
                elif(command == "3"):
                    os.system("docker ps -a")
                elif(command == "4"):
                    print("Enter any Container name : ",end="")
                    name = input()
                    print("Enter image name for launch : ",end="")
                    laun = input()
                    os.system("docker run -dit --name {} {}".format(name,laun))
                elif(command == "5"):
                    print("Enter container name to start : ",end="")
                    container = input()
                    os.system("docker start {}".format(container))
                elif(command == "6"):
                    print("Enter Container name to attach : ",end="")
                    cname = input()
                    os.system("docker attach {}".format(cname))
                elif(command == "7"):
                    print("Enter Container name to stop : ",end="")
                    ename = input()
                    os.system("docker stop {}".format(ename))
                elif(command =="8"):
                    print("Enter Container name to remove : ",end="")
                    rname = input()
                    os.system("docker rm {}".format(rname))
                elif(command =="9"):
                    print("Enter image name to remove : ",end="")
                    iname = input()
                    os.system("docker image rm {}".format(iname))
                elif(command == "start"):
                    os.system("systemctl start docker")
	
        

        if(command == "5"):
            while True :

                print('''\n --------AWS manager--------
                c:clear e:Back to main menu
                1.Create key-pair
                2.Create EBS Volume
                3.Create S3 Bucket
                4.Cloudfront distribution (need origin as s3)
                5.Attach ebs into EC2 instance (require vol. ID and instance ID)
                6.Show Instance Details
                7.Create EC2 Instance
                8.Create Security group
                
                ''')
                print("Enter Your option : ",end="")
                command = input()
                if(command == "1"):
                    print("enter name of the key given.",end='')
                    key_name=input()
                    os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
                elif(command == "2"):
                    print("Enter size of the ebs volume",end='')
                    size = input()
                    print("Enter region code i.e. us-east-1b")
                    az = input()
                    os.system("aws ec2 create-volume --size {} --availability-zone {}".format(size,az))                
                elif(command == "3"):
                    print("Enter bucket Name.",end="")
                    b_name=input()
                    print("Enter region code.",end="")
                    r_code=input()
                    os.system("aws s3api create-bucket --bucket {} --region {}".format(b_name,r_code))
                
                elif(command == "4"):
                    print("provide s3 origin domain url: ",end="")
                    s3_url = input()
                    print("Enter root object name (as in s3 bucket) : ",end="")
                    f_name = input()
                    os.system("aws cloudfront create-distribution --origin-domain-name {} --default-root-object {}".format(s3_url,f_name))
                elif(command == "5"):
                    print("Enter volume id",end='')
                    v_id=input()
                    print("Enter instance id",end="")
                    i_id=input()
                    os.system("aws ec2 attach-volume --device /dev/sdh --volume-id {} --instance-id {}".format(v_id,i_id))
                elif(command == "6"):
                    os.system("aws ec2 describe-instances")
                elif(command == "7"):
                    print("Enter AMI ID.",end='')
                    a_id=input()
                    print("Enter instance type",end='')
                    i_type=input()
                    print("Enter no. of instances to launce",end='')
                    count=input()
                    print("Enter subnet ID",end='')
                    s_id=input()
                    print("Enter security group ids",end='')
                    sg_id=input()
                    print("Enter valid key name",end="")
                    k_name=input()
                    os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}".format(a_id,i_type,count,s_id,sg_id,k_name))
                elif(command =="8"):
                    print("Enter name of security group",end="")
                    gname = input()
                    print("Enter description of security group",end="")
                    des = input()
                    des = "'"+des+"'"
                    os.system("aws ec2 create-security-group --group-name {} --description {}".format(gname,des))
                
                elif(command == "c"):
                    os.system("clear")
                elif(command == "e"):
                    os.system("clear")
                    break    
                
                
                        
                        