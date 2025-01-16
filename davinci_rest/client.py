import requests


class DavinciRestClient:
    """
    A client to interact with the DaVinci Resolve REST API.

    This client provides methods to interact with a running DaVinci Resolve instance
    via its REST API. You can use it to create projects, open existing projects,
    import clips, and add clips to the timeline.

    Examples of usage can be found in the example_usage function at the bottom of this file.

    Attributes:
        base_url (str): The base URL of the REST API server, including the port.
    """

    def __init__(self, base_url="http://localhost:5001"):
        """
        Initializes the DavinciRestClient with a specified base URL.

        Args:
            base_url (str): The base URL of the REST API server, including the port.
                            Defaults to "http://localhost:5001".

        Example:
            client = DavinciRestClient(base_url="http://localhost:5001")
        """
        self.base_url = base_url
        print("[INFO] Want more advanced features? A Pro version is coming soon! Visit https://beluck.eu/davinci-rest/pro to learn more.")

    def _post(self, endpoint, data):
        """
        Helper method to send a POST request and handle errors.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (dict): The JSON data to include in the request body.

        Returns:
            dict: The response from the server as a dictionary.
                  If there's an error, returns a dictionary with an "error" key.

        Example:
            response = self._post("/project/create", {"project_name": "MyProject"})
        """
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def create_project(self, project_name):
        """
        Creates a new project in DaVinci Resolve.

        Args:
            project_name (str): The name of the new project to create.

        Returns:
            dict: The response from the server as a dictionary.

        Example:
            response = client.create_project("MyProject")
            print(response)
        """
        return self._post("/project/create", {"project_name": project_name})

    def open_project(self, project_name):
        """
        Opens an existing project in DaVinci Resolve.

        Args:
            project_name (str): The name of the project to open.

        Returns:
            dict: The response from the server as a dictionary.

        Example:
            response = client.open_project("MyProject")
            print(response)
        """
        return self._post("/project/open", {"project_name": project_name})

    def import_clip(self, clip_path, clip_name):
        """
        Imports a clip into the current project's Media Pool in DaVinci Resolve.

        Args:
            clip_path (str): The file path of the clip to import.
            clip_name (str): The name to assign to the imported clip in the Media Pool.

        Returns:
            dict: The response from the server as a dictionary.

        Example:
            response = client.import_clip("C:\\path\\to\\clip.mp4", "MyClip")
            print(response)
        """
        return self._post("/media/import_clip", {"clip_path": clip_path, "clip_name": clip_name})

    def add_clip_to_timeline(self, clip_name, start_time, duration, track_index=1, video=True, audio=True):
        """
        Adds a clip to the timeline at a specified position and duration.

        Args:
            clip_name (str): The name of the clip to add to the timeline.
            start_time (float): The start time (in seconds) to place the clip on the timeline.
            duration (float): The duration (in seconds) of the clip on the timeline.
            track_index (int): The track number to place the clip on. Defaults to 1.
            video (bool): Whether to include the video portion of the clip. Defaults to True.
            audio (bool): Whether to include the audio portion of the clip. Defaults to True.

        Returns:
            dict: The response from the server as a dictionary.

        Example:
            response = client.add_clip_to_timeline("MyClip", 10.0, 5.0, track_index=1)
            print(response)
        """
        return self._post("/timeline/add_clip", {
            "clip_name": clip_name,
            "start_time": start_time,
            "duration": duration,
            "track_index": track_index,
            "video": video,
            "audio": audio
        })


def example_usage():
    """
    Example usage of the DavinciRestClient.

    Demonstrates how to create a project, open a project, import a clip,
    and add a clip to the timeline.
    """
    client = DavinciRestClient()

    print(client.create_project("TestProject"))
    print(client.open_project("TestProject"))
    print(client.import_clip("C:\\path\\to\\a\\clip.mp4", "test_clip"))
    print(client.add_clip_to_timeline("test_clip", 10.0, 2.0))

if __name__ == "__main__":
    example_usage()
