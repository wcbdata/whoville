# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClusterViewResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'secure': 'bool',
        'ambari_server_ip': 'str',
        'blueprint': 'BlueprintViewResponse',
        'host_groups': 'list[HostGroupViewResponse]',
        'shared_service_response': 'SharedServiceResponse'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'secure': 'secure',
        'ambari_server_ip': 'ambariServerIp',
        'blueprint': 'blueprint',
        'host_groups': 'hostGroups',
        'shared_service_response': 'sharedServiceResponse'
    }

    def __init__(self, id=None, name=None, description=None, status=None, secure=False, ambari_server_ip=None, blueprint=None, host_groups=None, shared_service_response=None):
        """
        ClusterViewResponse - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._secure = None
        self._ambari_server_ip = None
        self._blueprint = None
        self._host_groups = None
        self._shared_service_response = None

        if id is not None:
          self.id = id
        self.name = name
        if description is not None:
          self.description = description
        if status is not None:
          self.status = status
        if secure is not None:
          self.secure = secure
        if ambari_server_ip is not None:
          self.ambari_server_ip = ambari_server_ip
        if blueprint is not None:
          self.blueprint = blueprint
        if host_groups is not None:
          self.host_groups = host_groups
        if shared_service_response is not None:
          self.shared_service_response = shared_service_response

    @property
    def id(self):
        """
        Gets the id of this ClusterViewResponse.
        id of the resource

        :return: The id of this ClusterViewResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClusterViewResponse.
        id of the resource

        :param id: The id of this ClusterViewResponse.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ClusterViewResponse.
        name of the resource

        :return: The name of this ClusterViewResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClusterViewResponse.
        name of the resource

        :param name: The name of this ClusterViewResponse.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")
        if name is not None and len(name) < 5:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `5`")
        if name is not None and not re.search('(^[a-z][-a-z0-9]*[a-z0-9]$)', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/(^[a-z][-a-z0-9]*[a-z0-9]$)/`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ClusterViewResponse.
        description of the resource

        :return: The description of this ClusterViewResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ClusterViewResponse.
        description of the resource

        :param description: The description of this ClusterViewResponse.
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def status(self):
        """
        Gets the status of this ClusterViewResponse.
        status of the cluster

        :return: The status of this ClusterViewResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClusterViewResponse.
        status of the cluster

        :param status: The status of this ClusterViewResponse.
        :type: str
        """
        allowed_values = ["REQUESTED", "CREATE_IN_PROGRESS", "AVAILABLE", "UPDATE_IN_PROGRESS", "UPDATE_REQUESTED", "UPDATE_FAILED", "CREATE_FAILED", "ENABLE_SECURITY_FAILED", "PRE_DELETE_IN_PROGRESS", "DELETE_IN_PROGRESS", "DELETE_FAILED", "DELETE_COMPLETED", "STOPPED", "STOP_REQUESTED", "START_REQUESTED", "STOP_IN_PROGRESS", "START_IN_PROGRESS", "START_FAILED", "STOP_FAILED", "WAIT_FOR_SYNC", "MAINTENANCE_MODE_ENABLED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def secure(self):
        """
        Gets the secure of this ClusterViewResponse.
        tells wether the cluster is secured or not

        :return: The secure of this ClusterViewResponse.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """
        Sets the secure of this ClusterViewResponse.
        tells wether the cluster is secured or not

        :param secure: The secure of this ClusterViewResponse.
        :type: bool
        """

        self._secure = secure

    @property
    def ambari_server_ip(self):
        """
        Gets the ambari_server_ip of this ClusterViewResponse.
        public ambari ip of the stack

        :return: The ambari_server_ip of this ClusterViewResponse.
        :rtype: str
        """
        return self._ambari_server_ip

    @ambari_server_ip.setter
    def ambari_server_ip(self, ambari_server_ip):
        """
        Sets the ambari_server_ip of this ClusterViewResponse.
        public ambari ip of the stack

        :param ambari_server_ip: The ambari_server_ip of this ClusterViewResponse.
        :type: str
        """

        self._ambari_server_ip = ambari_server_ip

    @property
    def blueprint(self):
        """
        Gets the blueprint of this ClusterViewResponse.
        blueprint for the cluster

        :return: The blueprint of this ClusterViewResponse.
        :rtype: BlueprintViewResponse
        """
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint):
        """
        Sets the blueprint of this ClusterViewResponse.
        blueprint for the cluster

        :param blueprint: The blueprint of this ClusterViewResponse.
        :type: BlueprintViewResponse
        """

        self._blueprint = blueprint

    @property
    def host_groups(self):
        """
        Gets the host_groups of this ClusterViewResponse.
        collection of hostgroups

        :return: The host_groups of this ClusterViewResponse.
        :rtype: list[HostGroupViewResponse]
        """
        return self._host_groups

    @host_groups.setter
    def host_groups(self, host_groups):
        """
        Sets the host_groups of this ClusterViewResponse.
        collection of hostgroups

        :param host_groups: The host_groups of this ClusterViewResponse.
        :type: list[HostGroupViewResponse]
        """

        self._host_groups = host_groups

    @property
    def shared_service_response(self):
        """
        Gets the shared_service_response of this ClusterViewResponse.
        shared service for a specific stack

        :return: The shared_service_response of this ClusterViewResponse.
        :rtype: SharedServiceResponse
        """
        return self._shared_service_response

    @shared_service_response.setter
    def shared_service_response(self, shared_service_response):
        """
        Sets the shared_service_response of this ClusterViewResponse.
        shared service for a specific stack

        :param shared_service_response: The shared_service_response of this ClusterViewResponse.
        :type: SharedServiceResponse
        """

        self._shared_service_response = shared_service_response

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ClusterViewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
