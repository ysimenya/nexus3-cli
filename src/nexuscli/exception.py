from nexuscli.cli.errors import CliReturnCode


class NexusClientBaseError(Exception):
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.UNKNOWN_ERROR

    def __init__(self, *args, cli_return_code=None):
        super().__init__(*args)
        self.cli_return_code = cli_return_code or self.DEFAULT_CLI_RETURN_CODE


class NexusClientAPIError(NexusClientBaseError):
    """Unexpected response from Nexus service."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.API_ERROR


class NexusClientConnectionError(NexusClientBaseError):
    """Generic network connector error."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.CONNECTION_ERROR


class NexusClientInvalidCredentials(NexusClientBaseError):
    """
    Login credentials not accepted by Nexus service. Usually the result of a
    HTTP 401 response.
    """
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.INVALID_CREDENTIALS


class NexusClientInvalidRepositoryPath(NexusClientBaseError):
    """
    Used when an operation against the Nexus service uses an invalid or
    non-existent path.
    """
    pass


class NexusClientInvalidRepository(NexusClientBaseError):
    """The given repository does not exist in Nexus."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.REPOSITORY_NOT_FOUND


class NexusClientInvalidCleanupPolicy(NexusClientBaseError):
    """The given cleanup policy does not exist in Nexus."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.SUBCOMMAND_ERROR


class NexusClientCreateRepositoryError(NexusClientBaseError):
    """Used when a repository creation operation in Nexus fails."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.SUBCOMMAND_ERROR


class NexusClientCreateCleanupPolicyError(NexusClientBaseError):
    """Used when a cleanup policy creation operation in Nexus fails."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.SUBCOMMAND_ERROR


class DownloadError(NexusClientBaseError):
    """Error retrieving artefact from Nexus service."""
    DEFAULT_CLI_RETURN_CODE = CliReturnCode.DOWNLOAD_ERROR
