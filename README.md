# KAFKA-CC

![Kafka img](images/kafka.png?raw=true "Kafka")
![Kafka img2](images/kafka2.png?raw=true "Kafka2")

## Topics
A topic is a category or feed name to which records are published. Topics in Kafka are always multi-subscriber; that is, a topic can have zero, one, or many consumers that subscribe to the data written to it. A topic is identified by its name, which must be unique within a Kafka cluster. A topic is either configured to be retained forever or to be deleted after a certain time has elapsed.

![Kafka img3](images/topic.png?raw=true "Kafka3")

- Kafka is a distributed streaming platform. It is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

## Kafka topic partition
A topic is split into a number of partitions, which are distributed over the brokers in the cluster. Each partition is an ordered, immutable sequence of records that is continually appended to—a commit log. The records in the partitions are each assigned a sequential id number called the offset that uniquely identifies each record within the partition. Kafka uses this mechanism to provide the features and services described below.

![Kafka img4](images/partition.png?raw=true "Kafka4")

## Kafka Producer
A Kafka producer is a client that publishes records to the Kafka cluster. The producer is responsible for choosing which record will be assigned to which partition within the topic. If no partition is specified in the record, then the producer will use a partitioner to choose one. The partition is chosen by applying a hash function to the key of the record, or if the key is null then the producer will choose a partition in a round-robin fashion.

## Kafka Consumer
A Kafka consumer is a client that subscribes to a topic and processes the records that it receives. The consumer can either read the records in order, which is the default behavior, or skip around in the partition to consume only records that meet a certain filter criterion.

![Kafka img9](images/kafka3.png?raw=true "Kafka9")

## Kafka Consumer Group
A consumer group is a group of consumers that work together to consume messages from a Kafka topic. Each consumer in a group is assigned a subset of the partitions in the topic. The consumer group as a whole is responsible for consuming all the messages in the topic. If there are more partitions in the topic than there are consumers in the group, then some consumers will be assigned multiple partitions. If there are fewer partitions in the topic than there are consumers in the group, then some consumers will not be assigned any partitions.

![Kafka img10](images/kafka4.png?raw=true "Kafka10")

A consumer instance of same consumer group can be deployed on different machines. This is useful when you want to scale your consumer. You can add more instances of same consumer group to consume more messages.

![Kafka img11](images/kafka5.png?raw=true "Kafka11")
## Kafka in python

### bootstrap_servers
A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. This does not have to be the full node list. It just needs to have at least one broker that will respond to a Metadata API Request. The default port is 9092. If no servers are specified, it will default to localhost:9092.

### value_serializer
A function used to encode message values prior to serialization. If None, message values will be sent as raw bytes.

```
    pip install kafka-python # install kafka-python
    pip install faker # install faker for fake data
```

![Kafka img5](images/kafkaPython.png?raw=true "Kafka5")

# Zookeeper and Confluent

- Zookeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds make it a perfect fit for Kafka.

- Confluent is a company that provides a distribution of Apache Kafka that includes additional enterprise features and support. Confluent is the company behind the Kafka project and the Kafka community.

## Producer Example 1

![Kafka img6](images/example1.png?raw=true "Kafka6")

## Producer Example 2
![Kafka img7](images/example2.png?raw=true "Kafka7")

## Producer Example 3
![Kafka img8](images/example3.png?raw=true "Kafka8")

## Consumer Example 1
![Kafka img12](images/example4.png?raw=true "Kafka12")

## Docker-compose
To run the docker-compose file, you need to have docker and docker-compose installed on your machine.

``` 
    docker-compose -f docker-compose.yml up
```
