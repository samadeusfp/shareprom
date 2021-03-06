# ShareProm
This repository contains the source code of ShareProm, a Secure Multi-party computation system for Inter-organizational Process Mining. The system is still under development. A research publication is pending for the system by [Gamal Elkoumy](https://scholar.google.com/citations?user=Y1ze0vQAAAAJ&hl=en&oi=ao), [Stephan A. Fahrenkrog-Peterson](https://scholar.google.com/citations?user=Le-1B90AAAAJ&hl=en&oi=sra), [Marlon Dumas](https://scholar.google.com/citations?user=9lIttRkAAAAJ&hl=en&oi=ao) , [Peeter Laud](https://scholar.google.com/citations?user=3hc5DR8AAAAJ&hl=en&oi=ao), [Alisa Pankova](https://scholar.google.com/citations?user=KG2eH5sAAAAJ&hl=en&oi=ao) and [Matthias Weldich](https://scholar.google.com/citations?user=P_9a7I0AAAAJ&hl=en).

This repository contains scripts for the implementation of Shareprom and for performing the experimental evaluation of the system. The system is implemented on top of Sharemind [1], a secure multi-party computation engine. The system architecture and evaluation experiments are presented in the [paper](https://arxiv.org/abs/1912.01855)

To cite the project, you can use the following form:
```
@misc{elkoumy2019secure,
    title={Secure Multi-Party Computation for Inter-Organizational Process Mining},
    author={Gamal Elkoumy and Stephan A. Fahrenkrog-Petersen and Marlon Dumas and Peeter Laud and Alisa Pankova and Matthias Weildich},
    year={2019},
    eprint={1912.01855},
    archivePrefix={arXiv},
    primaryClass={cs.CR}
}
```
## System Requirement
The implementation of the system is in SecreC [2], a C++ like language that runs on top of Sharemind. The following are the required environmental setup for running the system:
* The installation of sharemind servers on 3 servers and the key authentication between the servers so they can communicate securely.
* Installation of sharemind client, that could be either on one of the 3 servers or a separate machine. Also, we need to share the key of the client on the 3 servers so they can trust the client applications.
* All the importing process of the CSV files should be performed using sharemind csv-importer. The CSV importer is only available for Academic and industrial licenses and we use our Academic license.
* The installation of linux package apt-transport-https

You can download a pre-installed sharemind virtual machine for free from sharemind's [website](https://sharemind.cyber.ee/).

Or, you can install sharemind on your own environment using [sharemind server installation guide](https://docs.sharemind.cyber.ee/2019.03/installation/application-server) and [client installation guide](https://docs.sharemind.cyber.ee/2019.03/installation/client-applications). After the instraction on the guides run the following command on the three servers to download the package ```libsharemind-mod-shared3pdev-ctrl```:

```
sudo apt-get install libsharemind-mod-shared3pdev-ctrl
```
And on the client's machine to enabling running the script using clients:
```
sudo apt-get install sharemind-runscript
```
## Data Format
The proposed approach assume the following:
* The data of partyA and partyB are loaded to the servers separately, each event log is in a separate file.
* To use the Outer product approach, the data should label the events in binary representation (0100), with each bit in a separate column.
* To use the parallel chunks, the data should include padding. The padding makes all the traces have the same length as the maximum length of traces of each party. 

Also, you can find preprocessing and data examples in python in the following directory:
```
shareprom/data_and_preprocessing/
```

## Running The System
The system runs as a client application on top of sharemind. You can submit your job using the following command:
```
sudo sharemind-runscript job_name.sb
```

## Experiment Setup
To be able to run the experiment, you need to make sure that profiling is enabled "Profiler=on", and install the package [nethogs](https://github.com/raboof/nethogs)

To run the experiment, use the shell script file:
```
shareprom/SecreC_implementation/experiment/experiment.sh
```

## Running Demo on Open VM
As mentioned above, to run the full system, you need to have Academic license. To make it easier for the reader, we prepared a demo that presents our work and could run on the Sharemind's open VM.

#### Instructions to open the demo on the Open sharemind VM:
* Get and install the virtual machine from [sharemind's website](https://sharemind.cyber.ee/)
* Run the Virtual Machine, download our GitHub repository to your VM, and Open the QT Creator
* You need to run the 3 computing servers on the machine. You can do that from `QT Creator > Tools > External > Sharemind SDK > start Sharemind`
* Now, you need to open the demo file in your editor. You can do that from `QT Creator > File > Open File or Project > Redirect to the demo folder > select demo.sc`
* To run the script, from `QT Creator > Tools > External > Sharemind SDK > Run SecreC`.

## References
[1] Archer, David W., et al. "From Keys to Databases—Real-World Applications of Secure Multi-Party Computation." The Computer Journal 61.12 (2018): 1749-1771.

[2] Bogdanov, Dan, Peeter Laud, and Jaak Randmets. "Domain-polymorphic language for privacy-preserving applications." Proceedings of the First ACM workshop on Language support for privacy-enhancing technologies. ACM, 2013.
